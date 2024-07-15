import streamlit as st
from django.core.wsgi import get_wsgi_application
from django.conf import settings
import os

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

# Import Django models and viewsets
from myapp.viewsets import MyModelViewSet

st.title('Django Integration with Streamlit')

# Streamlit app logic
def main():
    st.sidebar.title('Operations')
    operation = st.sidebar.selectbox("Select an operation", ["Create", "Retrieve"])

    # Initialize the viewset
    viewset = MyModelViewSet()

    if operation == "Create":
        st.header('Create Data in Django')

        # Input fields for creating new data
        name = st.text_input('Enter Name:')
        description = st.text_area('Enter Description:')

        # Button to create data
        if st.button('Create Data'):
            request_data = {'name': name, 'description': description}
            request = type('', (), {})()  # Create a dummy request object
            request.data = request_data
            response = viewset.create(request)
            if response.status_code == 201:
                st.success(f'Data created successfully')
            else:
                st.error(f'Failed to create data')

    elif operation == "Retrieve":
        st.header('Fetch Data from Django')

        # Button to fetch data
        if st.button('Fetch Data'):
            response = viewset.list(None)
            if response.status_code == 200:
                st.write('Fetched Data:')
                st.table(response.data)
            else:
                st.error(f'Failed to fetch data: {response.data}')

    # elif operation == "Update":
    #     st.header('Update Data in Django')

    #     # Input fields for updating data
    #     pk = st.number_input('Enter ID of the item to update:', min_value=1, step=1)
    #     new_name = st.text_input('Enter New Name:')
    #     new_description = st.text_area('Enter New Description:')

    #     # Button to update data
    #     if st.button('Update Data'):
    #         request_data = {'name': new_name, 'description': new_description}
    #         request = type('', (), {})()  # Create a dummy request object
    #         request.data = request_data
    #         response = viewset.update(request, pk=pk)
    #         if response.status_code == 200:
    #             st.success(f'Data updated successfully: {response.data}')
    #         else:
    #             st.error(f'Failed to update data: {response.data}')

    # elif operation == "Delete":
    #     st.header('Delete Data from Django')

    #     # Input field for deleting data
    #     del_pk = st.number_input('Enter ID of the item to delete:', min_value=1, step=1)

    #     # Button to delete data
    #     if st.button('Delete Data'):
    #         response = viewset.destroy(None, pk=del_pk)
    #         if response.status_code == 204:
    #             st.success('Data deleted successfully.')
    #         else:
    #             st.error('Failed to delete data.')

if __name__ == '__main__':
    main()
