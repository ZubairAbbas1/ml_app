export type StreamMode='horizontal'|'vertical'|'dual';
export type FitMode='fit'|'fill'|'stretch'|'original';
export type Encoder='auto'|'nvenc'|'qsv'|'amf'|'cpu';
export type StreamState='offline'|'preparing'|'connecting'|'streaming'|'reconnecting'|'stopping'|'error';
export interface MediaInfo{path:string;name:string;size:number;duration:number;width:number;height:number;fps:number;videoCodec:string;audioCodec?:string;audioChannels?:number;hasAudio:boolean}
export interface OutputConfig{enabled:boolean;server:string;key:string;width:number;height:number;fps:number;bitrateKbps:number;fit:FitMode;cropX:number;cropY:number;zoom:number}
export interface AppConfig{mode:StreamMode;loop:boolean;autoReconnect:boolean;adaptiveNetwork:boolean;encoder:Encoder;audioEnabled:boolean;audioVolume:number;rememberKeys:boolean;recordLocal:boolean;recordDir:string;horizontal:OutputConfig;vertical:OutputConfig}
export interface StreamStats{state:StreamState;fps:number;bitrateKbps:number;speed:string;frames:number;elapsed:number;reconnects:number;lastError?:string;targetBitrateKbps?:number;networkQuality?:'full'|'adaptive'|'recovery';playlistIndex?:number;connectedAt?:number}
