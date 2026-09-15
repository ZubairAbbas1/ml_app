import { contextBridge,ipcRenderer } from 'electron';
const listen=(channel:string,cb:any)=>{const f=(_:any,x:any)=>cb(x);ipcRenderer.on(channel,f);return()=>ipcRenderer.removeListener(channel,f)};
contextBridge.exposeInMainWorld('arsal',{
 openVideos:()=>ipcRenderer.invoke('video:openMany'),thumbnail:(p:string)=>ipcRenderer.invoke('video:thumbnail',p),chooseOverlay:()=>ipcRenderer.invoke('overlay:choose'),chooseDir:()=>ipcRenderer.invoke('dir:choose'),
 loadConfig:()=>ipcRenderer.invoke('config:load'),saveConfig:(c:any)=>ipcRenderer.invoke('config:save',c),preflight:(p:any)=>ipcRenderer.invoke('stream:preflight',p),start:(p:any)=>ipcRenderer.invoke('stream:start',p),stop:()=>ipcRenderer.invoke('stream:stop'),fixStream:()=>ipcRenderer.invoke('stream:fix'),switchScene:(s:string)=>ipcRenderer.invoke('scene:switch',s),networkAnalyze:(server:string)=>ipcRenderer.invoke('network:analyze',server),remux:(dir:string)=>ipcRenderer.invoke('recordings:remux',dir),exportDiagnostics:(d:any)=>ipcRenderer.invoke('diagnostics:export',d),
 onStats:(cb:any)=>listen('stream:stats',cb),onEvent:(cb:any)=>listen('stream:event',cb),systemInfo:()=>ipcRenderer.invoke('system:info')
});
