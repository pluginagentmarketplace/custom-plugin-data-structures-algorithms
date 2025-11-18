---
name: backend-fundamentals
description: Backend development fundamentals including API design, database management, and server architecture. Use when building REST APIs, GraphQL endpoints, or designing database schemas.
---

# Backend Development Fundamentals

## Quick Start

### Setting Up a Node.js Server

```javascript
const express = require('express');
const app = express();

app.use(express.json());

// REST API endpoint
app.get('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  // Database query here
  res.json({ id: userId, name: 'John Doe' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### Setting Up a Python Backend

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydb'
db = SQLAlchemy(app)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Database query
    return jsonify({'id': user_id, 'name': 'John Doe'})

if __name__ == '__main__':
    app.run(debug=True)
```

## API Design Best Practices

### RESTful Convention
- **GET** `/api/users` - List users
- **POST** `/api/users` - Create user
- **GET** `/api/users/:id` - Get user by ID
- **PUT** `/api/users/:id` - Update user
- **DELETE** `/api/users/:id` - Delete user

### Error Handling

```javascript
// Standard error response
app.use((err, req, res, next) => {
  const status = err.status || 500;
  const message = err.message || 'Internal Server Error';

  res.status(status).json({
    error: {
      status,
      message,
      timestamp: new Date().toISOString()
    }
  });
});
```

## Authentication & Security

### JWT Implementation

```javascript
const jwt = require('jsonwebtoken');

// Generate token
const generateToken = (userId) => {
  return jwt.sign({ userId }, 'your-secret-key', { expiresIn: '24h' });
};

// Verify middleware
const verifyToken = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decoded = jwt.verify(token, 'your-secret-key');
    req.userId = decoded.userId;
    next();
  } catch (err) {
    res.status(401).json({ error: 'Invalid token' });
  }
};
```

## Database Optimization

### SQL Indexing

```sql
-- Create index on frequently queried column
CREATE INDEX idx_users_email ON users(email);

-- Composite index for multiple columns
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Check query execution plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user@example.com';
```

### Connection Pooling

```javascript
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'mydb',
  password: 'password',
  port: 5432,
  max: 20,  // Maximum connection pool size
  idleTimeoutMillis: 30000,
});
```

## Caching Strategy

### Redis for Performance

```javascript
const redis = require('redis');
const client = redis.createClient();

app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  const cacheKey = `user:${userId}`;

  // Check cache
  const cachedUser = await client.get(cacheKey);
  if (cachedUser) {
    return res.json(JSON.parse(cachedUser));
  }

  // Query database
  const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);

  // Store in cache for 1 hour
  await client.setex(cacheKey, 3600, JSON.stringify(user));

  res.json(user);
});
```

## Testing Backend Code

### Unit Testing with Jest

```javascript
describe('User API', () => {
  test('should get user by ID', async () => {
    const response = await request(app).get('/api/users/1');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('id');
  });

  test('should return 404 for invalid user', async () => {
    const response = await request(app).get('/api/users/999');
    expect(response.status).toBe(404);
  });
});
```

## Key Concepts to Master

1. **HTTP Methods and Status Codes**
2. **Middleware Architecture**
3. **Database Normalization**
4. **Query Optimization**
5. **Connection Management**
6. **Error Handling Patterns**
7. **Logging and Monitoring**
8. **Rate Limiting**

## Further Reading

- REST API Design Rulebook
- Building Microservices by Sam Newman
- Database Performance Explained by Markus Winand