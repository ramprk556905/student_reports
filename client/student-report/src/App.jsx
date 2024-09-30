import { useState } from 'react'
import reactLogo from './assets/images/degree-cap-logo.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CreateStudent from './CreateStudent'
import {BrowserRouter as Router, Routes, Route,Link} from 'react-router-dom'

function App() {
  return (
    <Router>
      <div>
        <h1>Welcome to the Student Report Website</h1>
        {/* Use Link instead of button for navigation */}
        <Link to="/create-student">
          <button>Add Student</button>
        </Link>
      </div>

      {/* Define the Routes */}
      <Routes>
        <Route path="/create-student" element={<CreateStudent />} />
      </Routes>
    </Router>
  )
}

export default App
