"use client";

import { useState, useEffect } from 'react'
import { api } from '@/lib/api'

interface User {
  id: string
  email: string
  full_name?: string
}

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`
      api.get('/api/auth/me')
        .then(res => setUser(res.data.user))
        .catch(() => {
          localStorage.removeItem('token')
          delete api.defaults.headers.common['Authorization']
        })
        .finally(() => setLoading(false))
    } else {
      setLoading(false)
    }
  }, [])

  const login = async (email: string, password: string) => {
    const res = await api.post('/api/auth/login', { email, password })
    localStorage.setItem('token', res.data.access_token)
    api.defaults.headers.common['Authorization'] = `Bearer ${res.data.access_token}`
    setUser(res.data.user)
    return res.data
  }

  const register = async (data: { email: string; password: string; full_name?: string }) => {
    const res = await api.post('/api/auth/register', data)
    localStorage.setItem('token', res.data.access_token)
    api.defaults.headers.common['Authorization'] = `Bearer ${res.data.access_token}`
    setUser(res.data.user)
    return res.data
  }

  const logout = () => {
    localStorage.removeItem('token')
    delete api.defaults.headers.common['Authorization']
    setUser(null)
  }

  return { user, loading, login, register, logout }
}