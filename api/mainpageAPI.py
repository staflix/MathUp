from flask import render_template, redirect, request, make_response
from forms.mainpageForm import UnLogMainPageForm, LogMainPageForm
from flask_login import current_user
from data import db_session
from data.users import Info, User
from api.tituls import tituls
import flask

blueprint = flask.Blueprint(
    'main_page_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET', 'POST'])
def main_page_unlog():
    if not current_user.is_authenticated:
        form = UnLogMainPageForm()
        return render_template('unlog_index.html', form=form)
    else:
        visits_count = int(request.cookies.get("visits_count", 0))
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
        profile = LogMainPageForm()
        form = LogMainPageForm()
        page = 'main_page'

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()

        user_info = db_sess.query(Info).filter(current_user.id == Info.user_id).first()
        user_name = current_user.name
        user_surname = current_user.surname
        user_email = current_user.email
        user_avatar = user_info.avatar_href

        user = db_sess.query(User).filter(User.id == current_user.id).first()
        level = int(user.profile_level)

        db_sess.close()

        reg_now = request.args.get('reg') == 'True'

        if profile.settings.data:
            return redirect(f"/settings?next={page}")

        if profile.change_avatar.data:
            return redirect(f"/change_avatar?next={page}")

        if profile.exit.data:
            return redirect(f"/logout")

        if form.trainer_btn.data:
            return redirect(f"/choice_class")

        if form.company_btn.data:
            return redirect(f"/menu_company")
        return render_template('log_index.html', name=user_name, surname=user_surname, email=user_email,
                               avatar=user_avatar, profile=profile, form=form, reg_now=reg_now, level=level, tituls=tituls)
