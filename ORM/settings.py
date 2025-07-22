TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], 
            # Add the aerich.models to manage migrations
            # Run command: ```aerich init -t settings.TORTOISE_ORM```` to initialize migrations
            # Then run ```aerich init-db``` to create the initial tables in database
            # Run command: ```aerich migrate --name <migration_name>``` to create a migration file
            # Finally, run ```aerich upgrade``` to apply the migrations
            # You can also run ```aerich history``` to see the migration history
            # Run command: ```aerich downgrade``` to revert to a previous migration
            "default_connection": "default",
        }
    }
}
