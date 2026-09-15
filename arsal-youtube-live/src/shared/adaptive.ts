import type { OutputConfig, QualityStrategy, StreamHealth } from './types';

export type AdaptiveKind='horizontal'|'vertical';
export interface EffectiveProfile{width:number;height:number;fps:number;bitrateKbps:number;level:number;label:string}

const H=[
  {width:1920,height:1080,fps:30,bitrateKbps:10000,label:'1080p30 Full'},
  {width:1280,height:720,fps:30,bitrateKbps:4000,label:'720p30 Stable'},
  {width:960,height:540,fps:30,bitrateKbps:3000,label:'540p30 Recovery'},
  {width:640,height:360,fps:24,bitrateKbps:1800,label:'360p24 Emergency'},
];
const V=[
  {width:1080,height:1920,fps:30,bitrateKbps:10000,label:'1080x1920 Full'},
  {width:720,height:1280,fps:30,bitrateKbps:4000,label:'720x1280 Stable'},
  {width:540,height:960,fps:30,bitrateKbps:3000,label:'540x960 Recovery'},
  {width:360,height:640,fps:24,bitrateKbps:1800,label:'360x640 Emergency'},
];

export function initialAdaptiveLevel(strategy:QualityStrategy,safeMode:boolean){
  if(safeMode||strategy==='stable'||strategy==='weak')return 1;
  return 0;
}

export function effectiveProfile(kind:AdaptiveKind,base:OutputConfig,level:number,strategy:QualityStrategy,safeMode:boolean):EffectiveProfile{
  const ladder=kind==='horizontal'?H:V;
  const requested=Math.max(level,initialAdaptiveLevel(strategy,safeMode));
  const i=Math.max(0,Math.min(ladder.length-1,requested));
  const p=ladder[i];
  if(i===0)return{width:base.width,height:base.height,fps:base.fps,bitrateKbps:Math.min(base.bitrateKbps,p.bitrateKbps),level:i,label:p.label};
  return{...p,bitrateKbps:Math.min(base.bitrateKbps,p.bitrateKbps),level:i};
}

export function transportHealth(state:string,speed:number,reconnects:number):StreamHealth{
  if(state==='error')return'critical';
  if(state==='reconnecting')return'poor';
  if(state!=='streaming')return'idle';
  if(speed<0.8)return'critical';
  if(speed<0.95||reconnects>=3)return'poor';
  if(speed<0.99||reconnects>0)return'fair';
  return'excellent';
}

export function suggestedUploadMbps(kind:AdaptiveKind,profile:EffectiveProfile){
  const audio=.128,overhead=1.25;
  return Math.round((profile.bitrateKbps/1000+audio)*overhead*10)/10;
}

export function profileForUpload(kind:AdaptiveKind,uploadMbps:number,outputs=1){
  const ladder=kind==='horizontal'?H:V;
  const usable=Math.max(0,uploadMbps*.7/Math.max(1,outputs));
  for(let i=0;i<ladder.length;i++)if(ladder[i].bitrateKbps/1000<=usable)return{...ladder[i],level:i};
  return{...ladder[ladder.length-1],level:ladder.length-1};
}
