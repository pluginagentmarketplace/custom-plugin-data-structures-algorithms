---
name: system-architecture
description: System design principles, architectural patterns, scalability, and designing large-scale distributed systems.
---

# System Architecture Fundamentals

## Design Patterns

### Singleton Pattern

```typescript
class Database {
  private static instance: Database;

  private constructor() {}

  static getInstance(): Database {
    if (!this.instance) {
      this.instance = new Database();
    }
    return this.instance;
  }

  connect() {
    console.log('Connected to database');
  }
}

// Usage
const db1 = Database.getInstance();
const db2 = Database.getInstance();
console.log(db1 === db2); // true
```

### Observer Pattern

```typescript
interface Observer {
  update(data: any): void;
}

class Subject {
  private observers: Observer[] = [];

  subscribe(observer: Observer) {
    this.observers.push(observer);
  }

  notify(data: any) {
    this.observers.forEach(observer => observer.update(data));
  }
}

class Subscriber implements Observer {
  update(data: any) {
    console.log('Received update:', data);
  }
}
```

## Scalability Patterns

### Horizontal Scaling Architecture

```
┌─────────────┐
│  Load       │
│  Balancer   │
└──────┬──────┘
       │
   ┌───┼───┬───────┐
   │   │   │       │
┌──▼─┐│ ┌─┴──┐ ┌──▼──┐
│App │├─┤App │ │ App │
├────┤│ ├────┤ ├─────┤
│DB  │├─┤ DB │ │ DB  │
└────┘│ └────┘ └─────┘
      │
   Cache (Redis)
```

## Caching Strategy

### Multi-Level Caching

```python
class CacheManager:
    def __init__(self):
        self.l1_cache = {}  # In-memory
        self.redis_client = redis.Redis()  # L2

    def get(self, key):
        # Check L1
        if key in self.l1_cache:
            return self.l1_cache[key]

        # Check L2
        value = self.redis_client.get(key)
        if value:
            self.l1_cache[key] = value
            return value

        # Query database
        return None

    def set(self, key, value, ttl=3600):
        self.l1_cache[key] = value
        self.redis_client.setex(key, ttl, value)
```

## Database Sharding

### Sharding Strategy

```javascript
const getShardIndex = (userId) => {
  return userId % NUM_SHARDS;
};

const getShard = (userId) => {
  const shardIndex = getShardIndex(userId);
  return `shard_${shardIndex}`;
};

const getUserShard = async (userId) => {
  const shard = getShard(userId);
  const db = getDatabase(shard);
  return await db.query('SELECT * FROM users WHERE id = $1', [userId]);
};
```

## Load Balancing

### Round-Robin Algorithm

```javascript
class LoadBalancer {
  constructor(servers) {
    this.servers = servers;
    this.currentIndex = 0;
  }

  getNextServer() {
    const server = this.servers[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    return server;
  }
}
```

## API Design

### Rate Limiting

```javascript
const rateLimit = (req, res, next) => {
  const userId = req.user.id;
  const key = `rate_limit:${userId}`;

  redis.incr(key, (err, count) => {
    if (count === 1) {
      redis.expire(key, 60); // 1 minute window
    }

    if (count > 100) { // 100 requests per minute
      return res.status(429).json({ error: 'Too many requests' });
    }

    next();
  });
};
```

## Key Concepts

1. **Consistency Models (CAP Theorem)**
2. **Replication Strategies**
3. **Partitioning & Sharding**
4. **Load Balancing Algorithms**
5. **Caching Patterns**
6. **Rate Limiting**
7. **Circuit Breaker Pattern**