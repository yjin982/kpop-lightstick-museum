<script setup lang="ts">
import type { LightstickType } from '@/utils/types.ts'

interface Prop {
  lightStick: LightstickType
  url: string
  versions?: LightstickType[]
}

const { lightStick, url = '', versions = [] } = defineProps<Prop>()
</script>

<template>
  <div
    class="group relative w-52 h-78 bg-white rounded-lg shadow-xl overflow-hidden cursor-pointer"
  >
    <!-- 앞면 -->
    <div class="w-full h-full flex items-center justify-center relative">
      <img
        :src="lightStick.image"
        :alt="lightStick.artist"
        class="h-full object-contain px-2 items-center"
      />
    </div>

    <!-- 뒷면 -->
    <div
      class="absolute bg-white inset-0 flex flex-col gap-2 -translate-y-full transition-transform duration-500 ease-out group-hover:translate-y-0"
    >
      <div class="h-4/5 bg-zinc-100 flex items-center justify-center">
        <img :src="url" :alt="lightStick.artist" class="w-full h-full object-cover" />
      </div>
      <div class="h-1/5 pb-4">
        <div class="text-lg font-bold text-center text-gray-900">{{ lightStick.artist }}</div>
        <div class="text-sm text-center text-gray-600">{{ lightStick.agency }}</div>
      </div>
    </div>
  </div>
</template>
