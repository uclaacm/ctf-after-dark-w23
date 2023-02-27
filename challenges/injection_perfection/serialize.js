const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('app.db');

console.log('here');
console.log(process.env);

const users = [
	{ username: 'joe', password: 'bruin', fav_color: 'blue' },
	{ username: 'gamerboy80', password: 'bedwarsplayersarelikefliesexceptflies', fav_color: 'red' },
	{ username: 'admin', password: 'ad28b35084eabdb7edd22df20378748eb7575aef1342775f151efdc79abda430', fav_color: 'flag{red_is_the_best_color_fight_me_you_wont}' },
];

db.serialize(() => {
	db.run('CREATE TABLE users (username TEXT, password TEXT, fav_color TEXT)');
	const stmt = db.prepare('INSERT INTO users VALUES (?, ?, ?)');

	users.forEach(user => {
		stmt.run(user.username, user.password, user.fav_color);
	});

	stmt.finalize();
});