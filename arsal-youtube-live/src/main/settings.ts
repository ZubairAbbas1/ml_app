import { app,safeStorage } from 'electron';
import fs from 'fs';
import path from 'path';
import { defaultConfig } from '../shared/defaults';
import type { AppConfig } from '../shared/types';
const file=()=>path.join(app.getPath('userData'),'settings.json');
export function loadConfig():AppConfig{
 try{
  const x=JSON.parse(fs.readFileSync(file(),'utf8'));
  const c:AppConfig={...defaultConfig,...x,
   horizontal:{...defaultConfig.horizontal,...x.horizontal},vertical:{...defaultConfig.vertical,...x.vertical},
   audioProcessing:{...defaultConfig.audioProcessing,...x.audioProcessing},overlay:{...defaultConfig.overlay,...x.overlay},
   scenes:{...defaultConfig.scenes,...x.scenes},scheduler:{...defaultConfig.scheduler,...x.scheduler}
  };
  if(x.secureKeys&&safeStorage.isEncryptionAvailable()){
   const d=JSON.parse(safeStorage.decryptString(Buffer.from(x.secureKeys,'base64')));c.horizontal.key=d.h||'';c.vertical.key=d.v||'';
  }
  return c;
 }catch{return structuredClone(defaultConfig)}
}
export function saveConfig(c:AppConfig){
 const out:any={...c,horizontal:{...c.horizontal,key:''},vertical:{...c.vertical,key:''}};
 if(c.rememberKeys&&safeStorage.isEncryptionAvailable())out.secureKeys=safeStorage.encryptString(JSON.stringify({h:c.horizontal.key,v:c.vertical.key})).toString('base64');
 fs.mkdirSync(path.dirname(file()),{recursive:true});fs.writeFileSync(file(),JSON.stringify(out,null,2));
}
