def delete_user(request, user_id):
    user = get_object_or_404(EmployeeDetail, id=user_id)

    if request.method == 'POST':
        # Delete user and associated EmployeeDetail
        user.delete()
        return redirect('user_master')  # Redirect to a success page or wherever you want

    return render(request, 'delete_user.html', {'user': user})