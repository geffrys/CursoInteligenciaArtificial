import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { MusicExpertSystemFormComponent } from './components/music-expert-system-form/music-expert-system-form.component';
import { RecomendationListComponent } from './components/recomendation-list/recomendation-list.component';

@NgModule({
  declarations: [
    AppComponent,
    MusicExpertSystemFormComponent,
    RecomendationListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
