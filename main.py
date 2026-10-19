import sys

def generate_resume():
    print("=" * 60)
    print( "DEV MARKDOWN RESUME & BIO GENERATOR")
    print("=" * 60)

    name = input("Enter your full name or handle: ").strip()
    role = input("Enter your current role (e.g., Computer Science Student): ").strip()
    skills = input("Enter your key skills separated by commas (e.g., Python, Git, HTML/CSS): ").strip()
    project_name = input("Enter your best project name: ").strip()
    project_desc = input("Enter a one sentence description of that project: ").strip()
    email = input("Enter your contact email or LinkedIn URL: ").strip()

    skills_list = [s.strip() for s in skills.split(',')]
    formatted_skills = "\n- ".join(skills_list)

    resume_content = f"""# {name}

{role}

## Technical Skills
- {formatted_skills}

## Featured Projects
- **{project_name}:** {project_desc}

## Contact & Connect
- Reach out: {email}
"""
    filename = "RESUME.md"
    with open(filename, "w") as f:
        f.write(resume_content)

    print(f"\nSuccess! Your markdown resume has been generated and saved as '{filename}'.")

if __name__ == "__main__":
    generate_resume()