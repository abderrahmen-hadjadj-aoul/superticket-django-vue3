import axios from 'axios'

type Credentials = {
  username: string
  password: string
}

class ApiClient {
  axios = axios.create({
    baseURL: 'http://localhost:8000/'
  })

  async login(credentials: Credentials) {
    const response = await this.axios.post('api-token-auth/', credentials)
    const token = (response.data as any).token
    this.axios = axios.create({
      baseURL: 'http://localhost:8000/',
      headers: { Authorization: `Token ${token}` }
    })
  }
}

export const apiClient = new ApiClient()
