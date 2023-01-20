alter table 'order' add 'Transfer_stat';

CREATE TABLE Transfer(
	id INTEGER PRIMARY KEY,
	method_transfer TEXT default 'Post By',
	transfer_stat integer,
	FOREIGN KEY (transfer_stat) REFERENCES 'Order'(transfer_stat)
);