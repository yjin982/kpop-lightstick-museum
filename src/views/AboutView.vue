<script setup lang="ts">
import { ref } from 'vue'
import LightstickCard from '../components/lightsticks/LightstickCard.vue'
import lightsticks from '@/assets/lightsticks.json'
import type { LightstickType } from '@/utils/types.ts'

const items = ref<LightstickType[]>(lightsticks.lightsticks)
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <!-- 그리드 -->
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6"
      >
        <LightstickCard
          v-for="item in items"
          :key="item.id"
          :light-stick="item"
          :url="''"
          :ver="item.version"
        />
      </div>
    </div>
  </div>
</template>
