from db_utils import get_connection


def insert_job(job_data):

    try:
        conn = get_connection();
        cur = conn.cursor();

        query = """
        INSERT INTO jobs (title, company, job_location, job_type, job_description, skills, salary, experience_level, url, payment_type, payment_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """

        cur.execute(query, (
            job_data.get("title"),
            job_data.get("company"),
            job_data.get("job_location"),
            job_data.get("job_type"),
            job_data.get("job_description"),
            job_data.get("skills"),         # must be list for TEXT[]
            job_data.get("salary"),
            job_data.get("experience_level"),
            job_data.get("url"),
            job_data.get("payment_type"),
            job_data.get("payment_amount")
        ))

        job_id = cur.fetchone()[0]

        conn.commit() 
         
        cur.close()
        conn.close()

        return job_id
    
    except Exception as e:
        print("Error inserting job :" , e)
        return None
    
if __name__ == "__main__":
    new_job = {
        "title": "Data Engineer",
        "company": "TechCorp",
        "job_location": "Remote",
        "job_type": "Remote",   # must match ENUM options
        "job_description": "Build ETL pipelines for AI data.",
        "skills": ["Python", "SQL", "Airflow"],
        "salary": 80000,
        "experience_level": "Mid",
        "url": "https://example.com/job/123",
        "payment_type": None,
        "payment_amount": None
    }

    job_id = insert_job(new_job)
    print("Inserted Job ID:", job_id)