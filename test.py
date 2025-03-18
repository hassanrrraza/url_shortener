from app import app

# Print all registered routes
print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule.rule}")

# Run the app in test mode
if __name__ == "__main__":
    app.run(debug=True, port=5001) 