import time


products = {
    'laptop': 10,  # 10 units in stock
    'phone': 5,    # 5 units in stock
    'headphones': 0,  # 0 units, out of stock
    'tablet': 2,   # 2 units in stock
    'mouse': 15    # 15 units in stock
}

# Simple function to handle the chatbot response
def get_bot_reply(user_message):
    user_message = user_message.lower()

    
    if 'hello' in user_message or 'hi' in user_message:
        return "Hello! How can I assist you today?"
    
    # Handle store hours request
    elif 'store hours' in user_message:
        return "Our store is open from 9 AM to 9 PM every day!"

    # Handle product availability query
    elif 'product availability' in user_message:
        return "Please tell me the product name, and I will check availability for you."
    
    # Handle product search
    elif 'check availability' in user_message:
        product_name = user_message.split('check availability of')[-1].strip()
        return check_product_availability(product_name)
    
    # Handle feedback
    elif 'feedback' in user_message:
        return "Thank you for your feedback! We will make improvements based on it."
    
    # Handle exit
    elif 'exit' in user_message or 'bye' in user_message:
        return "Goodbye! Have a great day!"
    
    # Default fallback if input is not understood
    else:
        return "Sorry, I didn't quite understand that. Could you rephrase?"

# Function to check the availability of a product
def check_product_availability(product_name):
    product_name = product_name.lower()
    
    if product_name in products:
        stock = products[product_name]
        if stock > 0:
            return f"Yes, {product_name} is available! We have {stock} units in stock."
        else:
            return f"Sorry, {product_name} is currently out of stock."
    else:
        return f"Sorry, I couldn't find any product named {product_name} in our inventory."

# Main chatbot function
def start_chatbot():
    print("Welcome to the Catboat Chatbot!")
    time.sleep(1)
    print("I can assist you with some basic information.\nType 'exit' to end the chat.")
    
    while True:
        # Take user input
        user_input = input("\nYou: ")

        # Get response from the bot
        bot_reply = get_bot_reply(user_input)

        # Print the bot's reply
        print("Catboat: " + bot_reply)

        # Exit condition
        if 'exit' in user_input or 'bye' in user_input:
            break

    print("Chatbot session ended.")

if __name__ == "__main__":
    start_chatbot()
