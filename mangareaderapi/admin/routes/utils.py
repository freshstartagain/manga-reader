def check_existing_by_name(request, Model):
    if Model.query.filter_by(name=request).first():
        return True

