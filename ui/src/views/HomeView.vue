<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import Card from 'primevue/card'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

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
  <main class="flex flex-column align-items-center justify-content-center w-full h-full">
    <h1>SuperTicket</h1>
    <Card class="w-24rem">
      <template #content>
        <div v-if="hasWrongPassword" data-test="login-message">Wrong password</div>
        <div v-else class="login" data-test="login">
          <h1 data-test="login-title">Login</h1>
          <form>
            <div class="flex flex-column gap-2">
              <label for="username">Username</label>
              <InputText
                v-model="credentials.username"
                id="username"
                data-test="username"
                type="text"
              />
            </div>
            <div class="flex flex-column gap-2 mt-3">
              <label for="password">Password</label>
              <InputText
                v-model="credentials.password"
                id="password"
                data-test="password"
                type="password"
              />
            </div>
            <Button @click.prevent="login" data-test="button-login" class="mt-3">Login</Button>
          </form>
        </div>
      </template>
    </Card>
  </main>
</template>
