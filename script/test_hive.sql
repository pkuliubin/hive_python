select 
    transform(
            id,
            course_type,
            grades
        ) using "${hiveconf:HDFS_PYTHON} trans_grades.py"
as (id, course_type, grades, xuebu, new_grade)
from yuanfudao_course_all
where dt={@date}
