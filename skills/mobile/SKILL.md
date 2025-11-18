---
name: mobile-development
description: Mobile app development fundamentals for iOS and Android, including native and cross-platform approaches.
---

# Mobile Development Fundamentals

## iOS Development with Swift

### SwiftUI View

```swift
import SwiftUI

struct ContentView: View {
    @State private var users: [User] = []
    @State private var isLoading = false

    var body: some View {
        NavigationView {
            VStack {
                if isLoading {
                    ProgressView()
                } else {
                    List(users) { user in
                        NavigationLink(destination: UserDetailView(user: user)) {
                            VStack(alignment: .leading) {
                                Text(user.name)
                                    .font(.headline)
                                Text(user.email)
                                    .font(.caption)
                                    .foregroundColor(.gray)
                            }
                        }
                    }
                }
            }
            .navigationTitle("Users")
            .onAppear(perform: loadUsers)
        }
    }

    private func loadUsers() {
        isLoading = true
        // API call here
    }
}
```

## Android Development with Kotlin

### Jetpack Compose

```kotlin
@Composable
fun UserListScreen() {
    val users = remember { mutableStateOf(emptyList<User>()) }
    val isLoading = remember { mutableStateOf(false) }

    LaunchedEffect(Unit) {
        isLoading.value = true
        // Fetch users
    }

    if (isLoading.value) {
        CircularProgressIndicator()
    } else {
        LazyColumn {
            items(users.value) { user ->
                UserCard(user)
            }
        }
    }
}

@Composable
fun UserCard(user: User) {
    Card(modifier = Modifier.padding(8.dp)) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = user.name, style = MaterialTheme.typography.titleMedium)
            Text(text = user.email, style = MaterialTheme.typography.bodyMedium)
        }
    }
}
```

## Cross-Platform with React Native

### Functional Component

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, ActivityIndicator } from 'react-native';

export function UserListScreen() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch('/api/users');
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <ActivityIndicator size="large" />;
  }

  return (
    <FlatList
      data={users}
      renderItem={({ item }) => (
        <View style={{ padding: 10 }}>
          <Text style={{ fontSize: 16, fontWeight: 'bold' }}>{item.name}</Text>
          <Text style={{ color: '#666' }}>{item.email}</Text>
        </View>
      )}
      keyExtractor={(item) => item.id.toString()}
    />
  );
}
```

## Flutter Development

### Stateful Widget

```dart
class UserListScreen extends StatefulWidget {
  @override
  State<UserListScreen> createState() => _UserListScreenState();
}

class _UserListScreenState extends State<UserListScreen> {
  List<User> users = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchUsers();
  }

  void fetchUsers() async {
    final response = await http.get(Uri.parse('/api/users'));
    if (response.statusCode == 200) {
      setState(() {
        users = jsonDecode(response.body);
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Users')),
      body: isLoading
        ? Center(child: CircularProgressIndicator())
        : ListView.builder(
            itemCount: users.length,
            itemBuilder: (context, index) {
              final user = users[index];
              return ListTile(
                title: Text(user.name),
                subtitle: Text(user.email),
              );
            },
          ),
    );
  }
}
```

## Local Data Storage

### SQLite with Core Data (iOS)

```swift
import CoreData

class UserDataManager {
    static let shared = UserDataManager()
    let persistentContainer = NSPersistentContainer(name: "MyApp")

    func saveUser(_ user: User) {
        let entity = NSEntityDescription.entity(forEntityName: "User", in: persistentContainer.viewContext)!
        let newUser = NSManagedObject(entity: entity, insertInto: persistentContainer.viewContext)

        newUser.setValue(user.name, forKey: "name")
        newUser.setValue(user.email, forKey: "email")

        try? persistentContainer.viewContext.save()
    }
}
```

## Key Concepts

1. **UI Components & Layouts**
2. **State Management**
3. **Navigation & Routing**
4. **Network Requests**
5. **Local Storage**
6. **Permissions & Security**
7. **Performance Optimization**