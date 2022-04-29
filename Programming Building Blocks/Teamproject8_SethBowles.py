with open('hr_system.txt') as hr_file:
    for line in hr_file:
        line = line.strip()
        parts = line.split(' ')
        name = parts[0]
        id_number = int(parts[1])
        job_title = parts [2]
        salary = float(parts[3])
        salary = salary / 24
        if job_title == 'Engineer':
            salary = salary + 1000
            job_title = parts[2]
# print(f'Name: {name}, Title: {job_title}')
        print(f'{name} (ID: {id_number}), {job_title} - ${salary:,.2f}')
print ('Complete')