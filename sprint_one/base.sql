CREATE TYPE status_enum AS ENUM ('new', 'pending', 'accepted', 'rejected');

ALTER TABLE pereval_added
ADD COLUMN status status_enum NOT NULL DEFAULT 'new';


UPDATE pereval_added SET status = 'new' WHERE status IS NULL;