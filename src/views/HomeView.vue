<script setup lang="ts">
import { useLightstickStore } from '@/stores/useLightstickStore'
import { storeToRefs } from 'pinia'
import LightstickCard from '@/components/lightsticks/LightstickCard.vue'

const store = useLightstickStore()
const { groupedItems } = storeToRefs(store)
</script>

<template>
  <div class="home">
    <!-- 여기에 필터, 그리드, 페이지네이션 들어갈 예정 -->
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
      <LightstickCard
        v-for="group in groupedItems"
        :key="group.main.id"
        :light-stick="group.main"
        :versions="group.versions"
        :url="group.main?.profile ?? ''"
      />
    </div>
    <div>페이지네이션</div>
  </div>
</template>

<style scoped>
.home h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}
</style>
