<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()

import { apiClient } from '@/services/api-client'

const credentials = reactive({ username: '', password: '' })

const hasWrongPassword = ref(false)

async function login() {
  try {
    await apiClient.login(credentials)
    router.push({ name: 'dashboard' })
  } catch (e) {
    console.error(e)
    hasWrongPassword.value = true
  }
}
</script>

<template>
  <main>
    <div v-if="hasWrongPassword" data-test="login-message">Wrong password</div>
    <div v-else class="login" data-test="login">
      <h1 data-test="login-title">Login</h1>
      <form>
        <input v-model="credentials.username" data-test="username" type="text" />
        <input v-model="credentials.password" data-test="password" type="password" />
        <button @click.prevent="login" data-test="button-login">Login</button>
      </form>
    </div>
  </main>
</template>
