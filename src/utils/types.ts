export interface LightstickType {
  id: number
  artist: string
  name: string
  agency: string
  tag: string
  version: number
  group: boolean
  image: string
  profile?: string
}

export interface Filterd {
  main: LightstickType
  versions: LightstickType[]
}
