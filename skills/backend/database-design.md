---
name: database-design
description: Database schema design, normalization, relationships, and optimization. Use when designing relational databases, creating schemas, or optimizing queries.
---

# Database Design

## Normalization Levels

### First Normal Form (1NF)
- Atomic values only
- No repeating groups
- Each column has unique values

### Second Normal Form (2NF)
- Must satisfy 1NF
- Remove partial dependencies
- Non-key attributes depend on entire primary key

### Third Normal Form (3NF)
- Must satisfy 2NF
- Remove transitive dependencies
- Non-key attributes depend only on primary key

## Schema Design Example

```sql
-- Users Table (1NF, 2NF, 3NF)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts Table
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Comments Table
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  post_id INTEGER NOT NULL REFERENCES posts(id),
  user_id INTEGER NOT NULL REFERENCES users(id),
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Relationships

### One-to-Many
```sql
-- One user has many posts
ALTER TABLE posts
ADD CONSTRAINT fk_posts_user_id
FOREIGN KEY (user_id) REFERENCES users(id);
```

### Many-to-Many
```sql
CREATE TABLE post_tags (
  post_id INTEGER NOT NULL REFERENCES posts(id),
  tag_id INTEGER NOT NULL REFERENCES tags(id),
  PRIMARY KEY (post_id, tag_id)
);
```

## Indexing Strategy

```sql
-- Single column index
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- Composite index
CREATE INDEX idx_comments_post_user
ON comments(post_id, user_id);

-- Unique index
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Full text search index (PostgreSQL)
CREATE INDEX idx_posts_content_search
ON posts USING gin(to_tsvector('english', content));
```