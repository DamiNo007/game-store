export interface Game { 
    id:number;   
    full_name:string;
    short_name:string;
    price:number;
    genre: string;
    developer:string;
    publisher:string;
    release_date:Date;
    rating:number;
    description:string;
    img_path:string;
    video_path:string;
    os_min:string;
    processor_min:string;
    memory_min:string;
    graphics_min:string;
    space_min:string;
    os_opt:string;
    processor_opt:string;
    memory_opt:string;
    graphics_opt:string;
    space_opt:string;
    category:number;
}