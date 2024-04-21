export type User = {
    id: number;
    email: string;
    name: string;
    surname: string;
    patronim: string;
    role: {
        id: number;
        name: string;
        is_admin: boolean;
    };
};

/** Информация о текущем пользователе */
export async function fetchMe(): Promise<User> {
    return {
        id: 0,
        email: "test@test.com",
        name: "Иван",
        surname: "Иванов",
        patronim: "Иванович",
        role: {
            id: 0,
            name: "Администратор",
            is_admin: true
        }
    };
}

export async function fetchUsers(): Promise<User[]> {
    return [
        {
            id: 0,
            email: "test@test.com",
            name: "Иван",
            surname: "Иванов",
            patronim: "Иванович",
            role: {
                id: 0,
                name: "Администратор",
                is_admin: true
            }
        },
        {
            id: 1,
            email: "test@test.com",
            name: "Пётр",
            surname: "Иванов",
            patronim: "Иванович",
            role: {
                id: 1,
                name: "Аналитик",
                is_admin: false
            }
        },
        {
            id: 2,
            email: "test@test.com",
            name: "Иван",
            surname: "Петров",
            patronim: "Иванович",
            role: {
                id: 2,
                name: "Сотрудник склада",
                is_admin: true
            }
        }
    ];
}
