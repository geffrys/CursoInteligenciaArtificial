import { Component, OnInit } from '@angular/core';
import { ApiConsumeService } from '../services/api-consume.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit{

  constructor(private api:ApiConsumeService) { }

  genres: any;
  moods: any;

  result_playlist: any;

  onSubmit(data: any){
    console.log(data.value);
    this.api.evaluate(data.value).subscribe((data: any) => {
      this.result_playlist = data
      console.log(this.result_playlist);
    } , );
  }

  ngOnInit(): void {
    this.api.getMoods().forEach((data: any) => {
      this.moods = data;
    }, );
    this.api.getGenres().forEach((data: any) => {
      this.genres = data;
    }, );
  }

}
