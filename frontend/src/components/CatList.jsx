import React, { useEffect, useState } from 'react'
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

export default function CatList(){
  const [cats, setCats] = useState([])
  const [name, setName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(()=>{
    fetchCats()
  }, [])

  async function fetchCats(){
    setLoading(true)
    try{
      const res = await axios.get(`${API_BASE}/cats`)
      setCats(res.data || [])
    }catch(err){
      setError(err.message)
    }finally{
      setLoading(false)
    }
  }

  async function addCat(e){
    e.preventDefault()
    if(!name) return
    try{
      const res = await axios.post(`${API_BASE}/cats`, { name })
      setCats(prev=>[...prev, res.data])
      setName('')
    }catch(err){
      setError(err.message)
    }
  }

  async function deleteCat(id){
    try{
      const res = await axios.delete(`${API_BASE}/cats/${id}`)
      // on success remove from state
      setCats(prev => prev.filter(c => c.id !== id))
    }catch(err){
      setError(err.message)
    }
  }

  return (
    <div className="cat-list-root">
      <form onSubmit={addCat}>
        <input value={name} onChange={e=>setName(e.target.value)} placeholder="Enter cat name" />
        <button type="submit">Add</button>
      </form>

      {loading && <p>Loading...</p>}
      {error && <p style={{color:'red'}}>{error}</p>}

      <ul>
        {cats.map(c=> (
          <li key={c.id} style={{display:'flex', alignItems:'center', gap:8}}>
            <span style={{flex:1}}>{c.name}</span>
            <button onClick={() => deleteCat(c.id)} aria-label={`Delete ${c.name}`}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
