import { app,safeStorage } from 'electron';
import fs from 'fs';
import path from 'path';
import { defaultConfig } from '../shared/defaults';
import type { AppConfig,MultiDestination } from '../shared/types';
const file=()=>path.join(app.getPath('userData'),'settings.json');
export function loadConfig():AppConfig{
 try{
  const x=JSON.parse(fs.readFileSync(file(),'utf8'));
  const multi:MultiDestination[]=Array.isArray(x.multiDestinations)?x.multiDestinations.map((d:any)=>({id:String(d.id||''),name:String(d.name||'Channel'),kind:d.kind==='horizontal'?'horizontal':'vertical',enabled:d.enabled!==false,server:String(d.server||'rtmps://a.rtmps.youtube.com/live2'),key:''})):[];
  const c:AppConfig={...defaultConfig,...x,multiDestinations:multi,
   horizontal:{...defaultConfig.horizontal,...x.horizontal},vertical:{...defaultConfig.vertical,...x.vertical},
   audioProcessing:{...defaultConfig.audioProcessing,...x.audioProcessing},overlay:{...defaultConfig.overlay,...x.overlay},
   scenes:{...defaultConfig.scenes,...x.scenes},scheduler:{...defaultConfig.scheduler,...x.scheduler}
  };
  if(x.secureKeys&&safeStorage.isEncryptionAvailable()){
   const d=JSON.parse(safeStorage.decryptString(Buffer.from(x.secureKeys,'base64')));c.horizontal.key=d.h||'';c.vertical.key=d.v||'';
   const byId=new Map<string,string>((d.m||[]).map((z:any)=>[String(z.id),String(z.key||'')]));c.multiDestinations=c.multiDestinations.map(z=>({...z,key:byId.get(z.id)||''}));
  }
  return c;
 }catch{return structuredClone(defaultConfig)}
}
export function saveConfig(c:AppConfig){
 const out:any={...c,horizontal:{...c.horizontal,key:''},vertical:{...c.vertical,key:''},multiDestinations:c.multiDestinations.map(d=>({...d,key:''}))};
 if(c.rememberKeys&&safeStorage.isEncryptionAvailable())out.secureKeys=safeStorage.encryptString(JSON.stringify({h:c.horizontal.key,v:c.vertical.key,m:c.multiDestinations.map(d=>({id:d.id,key:d.key}))})).toString('base64');
 fs.mkdirSync(path.dirname(file()),{recursive:true});fs.writeFileSync(file(),JSON.stringify(out,null,2));
}
