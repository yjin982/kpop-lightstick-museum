<script setup lang="ts">
import { ref, onMounted } from 'vue'
import lightsticks from '@/assets/lightsticks.json'
import LightstickType from '@/utils/types.ts'

const items = ref<LightstickType[]>(lightsticks.lightsticks)
const test = ref<LightstickType>({
  id: 0,
  artist: '',
  name: '',
  agency: '',
  tag: '',
  version: 0,
  group: false,
  image: '',
})

onMounted(() => {
  test.value = items.value[2]
})
</script>

<template>
  <div class="card-container border border-gray-400 rounded-lg">
    <div class="card">
      <!-- 앞면: 응원봉 -->
      <div class="card-face front">
        <img :src="test.image" :alt="test.artist" />
      </div>

      <!-- 뒷면: 아티스트 사진 -->
      <div class="card-face back">
        <div class="flex flex-col h-full items-center">
          <img
            class="object-fit"
            src="https://search.pstatic.net/common?type=a&size=3000&quality=100&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2FprofileImg%2F5bab2299-e935-4295-85a1-949d9ff96572.jpg"
            :alt="test.artist"
          />
          <div>{{ test.artist }}</div>
          <div>{{ test.agency }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.card-container {
  perspective: 1000px;
  width: 17rem;
  height: 25rem;
  cursor: pointer;

  &:hover .card {
    transform: rotateY(180deg);
  }
}

.card {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
}

.card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  &.back {
    transform: rotateY(180deg);
  }
}
</style>
