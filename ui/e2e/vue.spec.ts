import { test, expect } from '@playwright/test'

function select(page: any, target: string) {
  return page.locator(`[data-test="${target}"]`)
}

async function login(page: any, username: string, password: string) {
  await expect(select(page, 'login-title')).toHaveText('Login')
  await select(page, 'username').fill(username)
  await select(page, 'password').fill(password)
  await select(page, 'button-login').click()
}

test('Login with wrong password', async ({ page }) => {
  await page.goto('/')
  await login(page, 'test', 'wrong-password')
  await expect(select(page, 'login-message')).toHaveText('Wrong password')
})

test('Login with correct password', async ({ page }) => {
  await page.goto('/')
  await login(page, 'test', 'test')
  await expect(select(page, 'main-title')).toHaveText('Dashboard')
})
