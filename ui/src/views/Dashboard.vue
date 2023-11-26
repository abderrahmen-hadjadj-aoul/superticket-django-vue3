<script setup lang="ts">
import { reactive } from 'vue'

import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Button from 'primevue/button'
import InlineMessage from 'primevue/inlinemessage'

import { apiClient } from '@/services/api-client'

const newTicket = reactive({ title: '', description: '' })

const message = reactive({ text: '', type: '' })

async function createTicket() {
  try {
    await apiClient.createTicket(newTicket)
    message.text = 'Ticket created'
    message.type = 'success'
  } catch (e) {
    message.text = 'Error while creating ticket'
    message.type = 'error'
  }
}
</script>

<template>
  <main>
    <h1 data-test="main-title">Dashboard</h1>
    <div>Create ticket</div>
    <form>
      <div class="flex flex-column">
        <label for="title">Title</label>
        <InputText v-model="newTicket.title" id="title" data-test="ticket-title" />
      </div>
      <div class="flex flex-column">
        <label for="description">Description</label>
        <Textarea
          v-model="newTicket.description"
          id="title-description"
          data-test="ticket-description"
        />
      </div>
      <Button @click.prevent="createTicket" data-test="ticket-button-create">Create</Button>
      <InlineMessage v-if="message.text" :severity="message.type" data-test="ticket-message">{{
        message.text
      }}</InlineMessage>
    </form>
  </main>
</template>
