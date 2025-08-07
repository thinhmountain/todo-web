import React, { useState } from 'react';

function TaskForm({ onAdd, apiUrl }) {
  const [title, setTitle] = useState('');
  const [deadline, setDeadline] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitting(true);
    fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, completed: false, deadline })
    })
      .then(res => res.json())
      .then(data => {
        onAdd({ id: data.id || Date.now(), title, completed: false, deadline });
        setTitle('');
        setDeadline('');
        setSubmitting(false);
      })
      .catch(() => setSubmitting(false));
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', gap: 8, marginBottom: 24 }}>
      <input
        type="text"
        placeholder="Task title"
        value={title}
        onChange={e => setTitle(e.target.value)}
        required
        style={{
          flex: 2,
          padding: 8,
          border: '1px solid #ccc',
          borderRadius: 4
        }}
      />
      <input
        type="date"
        value={deadline}
        onChange={e => setDeadline(e.target.value)}
        required
        style={{
          flex: 1,
          padding: 8,
          border: '1px solid #ccc',
          borderRadius: 4
        }}
      />
      <button
        type="submit"
        disabled={submitting}
        style={{
          padding: '8px 16px',
          background: '#1976d2',
          color: '#fff',
          border: 'none',
          borderRadius: 4,
          cursor: 'pointer'
        }}
      >
        {submitting ? 'Adding...' : 'Add'}
      </button>
    </form>
  );
}

export default TaskForm;
