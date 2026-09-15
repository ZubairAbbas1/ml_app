import type { AppConfig } from './types';
export const defaultConfig:AppConfig={
 mode:'dual',uiMode:'simple',qualityStrategy:'balanced',safeMode:false,previewQuality:'medium',loop:true,shuffle:false,autoReconnect:true,adaptiveNetwork:true,autoQualityRecovery:true,encoder:'auto',audioEnabled:true,audioVolume:100,audioProcessing:{limiter:true,compressor:false,noiseGate:false,gainDb:0},rememberKeys:false,recordLocal:false,recordDir:'',recordSegmentMinutes:60,autoRemux:false,overlay:{enabled:false,text:'',textSize:42,position:'bottom-right',imageEnabled:false,imagePath:'',imageScale:20,opacity:90},scenes:{startingText:'Starting Soon',brbText:'Be Right Back',endingText:'Thanks for watching'},scheduler:{enabled:false,autoStart:false,startTime:'',stopTime:'',weekdays:[0,1,2,3,4,5,6]},latencyPreference:'normal',uploadMbps:0,
 horizontal:{enabled:true,server:'rtmps://a.rtmps.youtube.com/live2',key:'',width:1920,height:1080,fps:30,bitrateKbps:10000,fit:'fit',cropX:50,cropY:50,zoom:100},
 vertical:{enabled:true,server:'rtmps://a.rtmps.youtube.com/live2',key:'',width:1080,height:1920,fps:30,bitrateKbps:10000,fit:'fill',cropX:50,cropY:50,zoom:100},
 multiDestinations:[]
};
