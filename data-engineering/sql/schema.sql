CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150),
    company VARCHAR(150),
    job_location VARCHAR(150),
    job_type VARCHAR(150) 
        DEFAULT 'Remote'
        CHECK (job_type IN ('Remote' , 'Hybrid' , 'On-site')),
    job_description TEXT,
    skills TEXT[],
    salary NUMERIC,                  -- optional (salary/budget)
    experience_level VARCHAR(100),   -- optional
    url TEXT UNIQUE,                 -- unique URL for the job post
    created_at TIMESTAMP DEFAULT NOW()

);



SELECT * FROM jobs;



