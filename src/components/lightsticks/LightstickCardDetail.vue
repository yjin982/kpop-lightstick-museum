<script setup lang="ts">
import { useLightstickStore } from '@/stores/useLightstickStore'
import { storeToRefs } from 'pinia'
import { GDialog } from 'gitart-vue-dialog'

const store = useLightstickStore()
const { isOpen, selectedItem } = storeToRefs(store)
</script>

<template>
  <div>
    <GDialog v-model="isOpen" width="1200">
      {{ selectedItem }}
    </GDialog>
  </div>
</template>

<style lang="scss" scoped></style>
