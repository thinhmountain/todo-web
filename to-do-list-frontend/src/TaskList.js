import React from 'react';

function TaskList({ tasks, onDelete, onToggle }) {
  if (!tasks.length) {
    return <p style={{ textAlign: 'center', color: '#888' }}>No tasks yet.</p>;
  }

  return (
    <ul style={{ listStyle: 'none', padding: 0 }}>
      {tasks.map(task => (
        <li
          key={task.id}
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '10px 0',
            borderBottom: '1px solid #eee'
          }}
        >
          <div style={{ flex: 1 }}>
            <span
              style={{
                textDecoration: task.completed ? 'line-through' : 'none',
                color: task.completed ? '#888' : '#222',
                fontWeight: 500
              }}
            >
              {task.title}
            </span>
            <span style={{
              marginLeft: 12,
              fontSize: 13,
              color: '#888'
            }}>
              (Deadline: {task.deadline})
            </span>
          </div>
          <div>
            <button
              onClick={() => onToggle(task.id, task.completed)}
              style={{
                marginRight: 8,
                padding: '4px 10px',
                background: task.completed ? '#ffc107' : '#4caf50',
                color: '#fff',
                border: 'none',
                borderRadius: 4,
                cursor: 'pointer'
              }}
            >
              {task.completed ? 'Undo' : 'Done'}
            </button>
            <button
              onClick={() => onDelete(task.id)}
              style={{
                padding: '4px 10px',
                background: '#e53935',
                color: '#fff',
                border: 'none',
                borderRadius: 4,
                cursor: 'pointer'
              }}
            >
              Delete
            </button>
          </div>
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
