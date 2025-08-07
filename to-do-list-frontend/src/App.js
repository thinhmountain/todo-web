import React, { useState, useEffect } from 'react';
import TaskList from './TaskList';
import TaskForm from './TaskForm';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  // Đổi port nếu backend chạy ở port khác
  const API_URL = 'http://localhost:5500/api/tasks';

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        setTasks(data);
        setLoading(false);
      })
      .catch(err => {
        setLoading(false);
        setTasks([]);
      });
  }, []);

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  const deleteTask = (id) => {
    fetch(`${API_URL}/${id}`, { method: 'DELETE' })
      .then(res => {
        if (res.ok) setTasks(tasks.filter(task => task.id !== id));
      });
  };

  const toggleComplete = (id, completed) => {
    fetch(`${API_URL}/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: !completed })
    })
      .then(res => {
        if (res.ok) {
          setTasks(tasks.map(task =>
            task.id === id ? { ...task, completed: !completed } : task
          ));
        }
      });
  };

  return (
    <div style={{
      maxWidth: 500,
      margin: '40px auto',
      padding: 24,
      background: '#fff',
      borderRadius: 10,
      boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
    }}>
      <h1 style={{ textAlign: 'center', color: '#1976d2' }}>📝 To-Do List</h1>
      <TaskForm onAdd={addTask} apiUrl={API_URL} />
      {loading ? (
        <p style={{ textAlign: 'center' }}>Loading...</p>
      ) : (
        <TaskList
          tasks={tasks}
          onDelete={deleteTask}
          onToggle={toggleComplete}
        />
      )}
    </div>
  );
}

export default App;
