export type StreamMode='horizontal'|'vertical'|'dual';
export type FitMode='fit'|'fill'|'stretch'|'original';
export type Encoder='auto'|'nvenc'|'qsv'|'amf'|'cpu';
export type StreamState='offline'|'preparing'|'connecting'|'streaming'|'reconnecting'|'stopping'|'error';
export type StreamHealth='idle'|'excellent'|'fair'|'poor'|'critical';
export type UiMode='simple'|'pro';
export type QualityStrategy='best'|'balanced'|'stable'|'weak';
export type PreviewQuality='low'|'medium'|'high';
export type SceneType='video'|'starting'|'brb'|'ending';
export type LatencyPreference='normal'|'low'|'ultra';
export type OutputKind='horizontal'|'vertical';
export interface MediaInfo{path:string;name:string;size:number;duration:number;width:number;height:number;fps:number;videoCodec:string;audioCodec?:string;audioChannels?:number;hasAudio:boolean}
export interface OutputConfig{enabled:boolean;server:string;key:string;width:number;height:number;fps:number;bitrateKbps:number;fit:FitMode;cropX:number;cropY:number;zoom:number}
export interface MultiDestination{id:string;name:string;kind:OutputKind;enabled:boolean;server:string;key:string}
export interface AudioProcessing{limiter:boolean;compressor:boolean;noiseGate:boolean;gainDb:number}
export interface OverlayConfig{enabled:boolean;text:string;textSize:number;position:'top-left'|'top-right'|'bottom-left'|'bottom-right'|'center';imageEnabled:boolean;imagePath:string;imageScale:number;opacity:number}
export interface SceneConfig{startingText:string;brbText:string;endingText:string}
export interface SchedulerConfig{enabled:boolean;autoStart:boolean;startTime:string;stopTime:string;weekdays:number[]}
export interface AppConfig{
 mode:StreamMode;uiMode:UiMode;qualityStrategy:QualityStrategy;safeMode:boolean;previewQuality:PreviewQuality;loop:boolean;shuffle:boolean;autoReconnect:boolean;adaptiveNetwork:boolean;autoQualityRecovery:boolean;encoder:Encoder;audioEnabled:boolean;audioVolume:number;audioProcessing:AudioProcessing;rememberKeys:boolean;recordLocal:boolean;recordDir:string;recordSegmentMinutes:number;autoRemux:boolean;overlay:OverlayConfig;scenes:SceneConfig;scheduler:SchedulerConfig;latencyPreference:LatencyPreference;uploadMbps:number;horizontal:OutputConfig;vertical:OutputConfig;multiDestinations:MultiDestination[]
}
export interface StreamStats{state:StreamState;health?:StreamHealth;fps:number;bitrateKbps:number;speed:string;frames:number;elapsed:number;reconnects:number;droppedFrames?:number;lastError?:string;lastWarning?:string;targetBitrateKbps?:number;networkQuality?:'full'|'adaptive'|'recovery'|'emergency';playlistIndex?:number;connectedAt?:number;adaptiveLevel?:number;effectiveWidth?:number;effectiveHeight?:number;effectiveFps?:number;profileLabel?:string;currentScene?:SceneType;sessionBytes?:number;destinationCount?:number}
export interface SessionEvent{time:number;level:'info'|'success'|'warning'|'error';message:string}
