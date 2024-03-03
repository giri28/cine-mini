from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

movies = {
    "1": {"title": "Avengers: Endgame", "showtimes": ["12:00 PM", "3:00 PM", "6:00 PM"], "seats": 300},
    "2": {"title": "The Shawshank Redemption", "showtimes": ["1:00 PM", "4:00 PM", "7:00 PM"], "seats": 250},
    "3": {"title": "The Godfather", "showtimes": ["2:00 PM", "5:00 PM", "8:00 PM"], "seats": 120}
}

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/book', methods=['POST'])
def book():
    movie_id = request.form['movie_id']
    showtime = request.form['showtime']
    num_tickets = int(request.form['num_tickets'])
    
    if movie_id not in movies:
        return render_template('error.html', message='Movie not found')

    if showtime not in movies[movie_id]['showtimes']:
        return render_template('error.html', message='Showtime not available for this movie')

    if num_tickets <= 0:
        return render_template('error.html', message='Invalid number of tickets')

    available_seats = movies[movie_id]['seats']
    if num_tickets > available_seats:
        return render_template('error.html', message=f'Only {available_seats} seats available')

    # Here, you can integrate with a ticket booking system and handle the booking process

    movies[movie_id]['seats'] -= num_tickets
    remaining_seats = movies[movie_id]['seats']

    return render_template('success.html', message='Booking successful!', remaining_seats=remaining_seats)

if __name__ == '__main__':
    app.run(debug=True)
