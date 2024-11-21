import axios from 'axios';
async function loginRequest() {
    try {
        const response = await axios({
            method: 'post',
            baseURL: 'http://localhost:8080',
            url: '/login',
            data: {
                username: 'capybanaa',
                password: '123456',
            },
        });
        console.log('User data:', response.data);
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}
