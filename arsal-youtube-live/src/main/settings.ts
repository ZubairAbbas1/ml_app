import { app,safeStorage } from 'electron';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { defaultConfig } from '../shared/defaults';
import type { AppConfig,MultiDestination } from '../shared/types';
const file=()=>path.join(app.getPath('userData'),'settings.json');
const token=()=>crypto.randomBytes(18).toString('base64url');
export function loadConfig():AppConfig{
 try{
  const x=JSON.parse(fs.readFileSync(file(),'utf8'));
  const multi:MultiDestination[]=Array.isArray(x.multiDestinations)?x.multiDestinations.map((d:any)=>({id:String(d.id||crypto.randomUUID()),name:String(d.name||'Channel'),kind:d.kind==='horizontal'?'horizontal':'vertical',enabled:d.enabled!==false,server:String(d.server||'rtmps://a.rtmps.youtube.com/live2'),key:'',priority:['primary','backup'].includes(d.priority)?d.priority:'normal',group:String(d.group||'Default')})):[];
  const c:AppConfig={...defaultConfig,...x,multiDestinations:multi,
   horizontal:{...defaultConfig.horizontal,...x.horizontal},vertical:{...defaultConfig.vertical,...x.vertical},
   audioProcessing:{...defaultConfig.audioProcessing,...x.audioProcessing},backgroundAudio:{...defaultConfig.backgroundAudio,...x.backgroundAudio},overlay:{...defaultConfig.overlay,...x.overlay},
   scenes:{...defaultConfig.scenes,...x.scenes},scheduler:{...defaultConfig.scheduler,...x.scheduler},remoteControl:{...defaultConfig.remoteControl,...x.remoteControl,token:''},studio:{...defaultConfig.studio,...x.studio}
  };
  if(x.secureKeys&&safeStorage.isEncryptionAvailable()){
   const d=JSON.parse(safeStorage.decryptString(Buffer.from(x.secureKeys,'base64')));c.horizontal.key=d.h||'';c.vertical.key=d.v||'';
   const byId=new Map<string,string>((d.m||[]).map((z:any)=>[String(z.id),String(z.key||'')]));c.multiDestinations=c.multiDestinations.map(z=>({...z,key:byId.get(z.id)||''}));c.remoteControl.token=d.remote||token();
  }else c.remoteControl.token=token();
  return c;
 }catch{const c=structuredClone(defaultConfig);c.remoteControl.token=token();return c}
}
export function saveConfig(c:AppConfig){
 const out:any={...c,horizontal:{...c.horizontal,key:''},vertical:{...c.vertical,key:''},multiDestinations:c.multiDestinations.map(d=>({...d,key:''})),remoteControl:{...c.remoteControl,token:''}};
 if(safeStorage.isEncryptionAvailable())out.secureKeys=safeStorage.encryptString(JSON.stringify({h:c.rememberKeys?c.horizontal.key:'',v:c.rememberKeys?c.vertical.key:'',m:c.rememberKeys?c.multiDestinations.map(d=>({id:d.id,key:d.key})):[],remote:c.remoteControl.token||token()})).toString('base64');
 fs.mkdirSync(path.dirname(file()),{recursive:true});fs.writeFileSync(file(),JSON.stringify(out,null,2));
}
