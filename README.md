# dojiket
a ticketing app for everyone by Kreative Dojo

## Prerequisites

- Docker
- Docker Compose

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/kreativedojo/dojiket.git
   cd dojiket
   ```

2. Start the containers:
   ```bash
   docker-compose up --build
   ```

## Accessing the Services

- API: http://localhost:8080
- pgAdmin: http://localhost:5050
  - Email: admin@admin.com
  - Password: admin

## Database Connection (via pgAdmin)

1. Login to pgAdmin
2. Right-click "Servers" → "Register" → "Server"
3. General tab:
   - Name: Event DB (or any name)
4. Connection tab:
   - Host: db
   - Port: 5432
   - Database: eventdb
   - Username: postgres
   - Password: postgres

## Stopping the Project

```bash
docker-compose down
```

To remove volumes (database data):
```bash
docker-compose down -v
```
