export interface User {
    id:number;
    password: string;
    last_login:string;
    is_superuser:boolean;
    first_name:string;
    last_name:string;
    email:string;
    is_staff:string;
    is_active:string;
}

export class UserClass{
    id:number;
    password: string;
    last_login:string;
    is_superuser:boolean;
    first_name:string;
    last_name:string;
    email:string;
    is_staff:string;
    is_active:string;

    constructor(jsonStr: string) {
        let jsonObj: any = JSON.parse(jsonStr);
        for (let prop in jsonObj) {
            this[prop] = jsonObj[prop];
        }
    }
}