from flask import render_template, request, redirect
import flask
from forms.company_levelForm import CompanyLevelForm
from data import db_session
from data.users import Info
from company.company_second_class import *
from company.company_first_class import *
from company.company_third_class import *
from company.company_fourth_class import *
from flask_login import current_user

blueprint = flask.Blueprint(
    'start_level_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/start_level/<level>', methods=['GET', 'POST'])
def start_level(level):
    form = CompanyLevelForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()

    if 1 <= int(level) <= 100:
        user_info.current_level = int(level)
        db_sess.commit()
        db_sess.close()
        timer, topic, tasks, answers, choices, imgs = get_level_data(year_1, level)
        return render_template("level.html", timer=timer, choice=choices, imgs=imgs,
                               topic=topic, tasks=tasks, answers=answers, form=form)

    elif 101 <= int(level) <= 200:
        user_info.current_level = int(level)
        db_sess.commit()
        db_sess.close()
        timer, topic, tasks, answers, choices, imgs = get_level_data(year_2, level)
        return render_template("level.html", timer=timer, choice=choices, imgs=imgs,
                               topic=topic, tasks=tasks, answers=answers, form=form)

    elif 201 <= int(level) <= 300:
        user_info.current_level = int(level)
        db_sess.commit()
        db_sess.close()
        timer, topic, tasks, answers, choices, imgs = get_level_data(year_3, level)
        return render_template("level.html", timer=timer, choice=choices, imgs=imgs,
                               topic=topic, tasks=tasks, answers=answers, form=form)

    elif 301 <= int(level) <= 400:
        user_info.current_level = int(level)
        db_sess.commit()
        db_sess.close()
        timer, topic, tasks, answers, choices, imgs = get_level_data(year_4, level)
        return render_template("level.html", timer=timer, choice=choices, imgs=imgs,
                               topic=topic, tasks=tasks, answers=answers, form=form)


def get_level_data(year, level_selected):
    topic_index = (int(level_selected) // 10) % 10
    level_within_topic_index = (int(level_selected) - 1) % 10
    if int(level_selected) % 10 == 0 and int(level_selected) % 100 != 0:
        topic_index -= 1
    elif int(level_selected) % 10 == 0 and int(level_selected) % 100 == 0:
        topic_index = 9

    selected_topic = year.topics[topic_index]
    selected_level = selected_topic.levels[level_within_topic_index]

    timer = selected_level.time
    topic = selected_topic.name
    tasks = [task.task for task in selected_level.tasks]
    answers = [task.answer for task in selected_level.tasks]
    choices = [task.choice if task.choice else None for task in selected_level.tasks]
    imgs = [task.image if task.image else None for task in selected_level.tasks]

    return timer, topic, tasks, answers, choices, imgs
