---
name: frontend-fundamentals
description: Modern frontend development using React, Vue, or Angular. Covers component creation, state management, hooks, and best practices for building user interfaces.
---

# Frontend Development Fundamentals

## React Quick Start

### Functional Component with Hooks

```jsx
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

export default UserProfile;
```

## Component Best Practices

### Single Responsibility Principle
```jsx
// ✅ Good - Single responsibility
function UserCard({ user }) {
  return (
    <div className="card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}

function UserList({ users }) {
  return (
    <div>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}
```

## State Management with Context

```jsx
const UserContext = React.createContext();

function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

function useUser() {
  const context = React.useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within UserProvider');
  }
  return context;
}
```

## Performance Optimization

### Code Splitting with React.lazy

```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));
const Settings = React.lazy(() => import('./Settings'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

### Memoization

```jsx
// Prevent unnecessary re-renders
const UserCard = React.memo(({ user }) => {
  return <div>{user.name}</div>;
});

// useMemo for expensive calculations
function ProcessedData({ data }) {
  const processed = React.useMemo(() => {
    return data.map(item => expensiveOperation(item));
  }, [data]);

  return <div>{processed.length} items</div>;
}
```

## Responsive Design with Tailwind CSS

```jsx
function ResponsiveCard() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-bold mb-2">Title</h3>
        <p className="text-gray-600">Content</p>
      </div>
    </div>
  );
}
```

## Testing Components

```jsx
import { render, screen } from '@testing-library/react';

describe('UserCard', () => {
  test('renders user information', () => {
    const user = { id: 1, name: 'John Doe' };
    render(<UserCard user={user} />);

    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});
```

## Key Concepts to Master

1. **Functional Components & Hooks**
2. **Component Composition**
3. **State Management**
4. **Props and PropTypes**
5. **Event Handling**
6. **Conditional Rendering**
7. **Form Handling**
8. **API Integration**