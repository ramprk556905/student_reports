import React, { useState } from 'react';
import api from './api';

function CreateStudent() {
  // Initialize state for all fields
  const [student, setStudent] = useState({
    roll_num: '',
    name: '',
    regn_num: '',
    dob: '',
    email: '',
    dept: ''
  });

  // Handle input changes
  const handleChange = (e) => {
    setStudent({ ...student, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/v1/create_student', student);
      alert('Student created successfully!');
      console.log(response.data);
    } catch (error) {
      console.error(error);
      alert(error.response.data.detail);
    }
  };

  return (
    <>
    <h1>Add Students Details here:</h1>
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        name="roll_num" 
        placeholder="Roll Number" 
        value={student.roll_num} 
        onChange={handleChange} 
        required 
      />
      <input 
        type="text" 
        name="name" 
        placeholder="Name" 
        value={student.name} 
        onChange={handleChange} 
        required 
      />
      <input 
        type="text" 
        name="regn_num" 
        placeholder="Registration Number" 
        value={student.regn_num} 
        onChange={handleChange} 
        required 
      />
      <input 
        type="date" 
        name="dob" 
        placeholder="Date of Birth" 
        value={student.dob} 
        onChange={handleChange} 
        required 
      />
      <input 
        type="email" 
        name="email" 
        placeholder="Email" 
        value={student.email} 
        onChange={handleChange} 
        required 
      />
      <input 
        type="text" 
        name="dept" 
        placeholder="Department" 
        value={student.dept} 
        onChange={handleChange} 
        required 
      />
      <button type="submit">Create Student</button>
    </form>
    </>
  );
}

export default CreateStudent;
